import { NextRequest, NextResponse } from 'next/server'
import { OpenAIStream, StreamingTextResponse } from "ai"
import OpenAI from "openai"

export const runtime = "edge"

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!,
})

export async function POST(req: NextRequest) {
  // Extract the `ingredient` from the body of the request
  const { ingredient } = await req.json()

  // Prompt to check if the ingredient is valid
  const prompt = `Is "${ingredient}" a valid and commonly used ingredient in cooking? Answer with "yes" or "no".`

  // Request the OpenAI API for the response based on the prompt
  const response = await openai.chat.completions.create({
    model: "gpt-3.5-turbo-1106",
    temperature: 0.6,
    frequency_penalty: 0.2,
    presence_penalty: 0.3,
    max_tokens: 10,
    stream: false,
    n: 1,
    messages: [
      { role: "user", content: prompt },
    ],
  })

  const answer = response.choices[0].message?.content?.trim().toLowerCase()

  // Ensure we return a valid response
  if (answer === "yes" || answer === "no") {
    return NextResponse.json({ content: answer })
  } else {
    console.error(`Unexpected API response: ${answer}`)
    return NextResponse.json({ content: "no" }) // Default to "no" if unexpected format
  }
}
