# Gastrono Genius

Gastrono Genius is an innovative project that leverages the clever and creative abilities of a GPT generator, built from scratch. This project involves creating a compact GPT model specifically tailored for the culinary domain, designed to offer a variety of services to enhance the cooking and dining experience.

## Project Overview

Gastrono Genius aims to revolutionize the culinary world by providing a suite of intelligent services powered by an advanced GPT model. The model is designed to understand and generate high-quality, context-aware content related to food and cooking. Key services include:

Recipe Generation: Create personalized recipes based on user preferences, dietary restrictions, and available ingredients.
Cooking Tips: Offer expert cooking tips and techniques to help users improve their culinary skills.
Nutritional Information: Provide detailed nutritional information for recipes and individual ingredients.
Meal Planning: Assist users in planning balanced and diverse meals for any occasion.
Ingredient Substitution: Suggest alternative ingredients for recipes based on availability and dietary needs.


## Features

- **Framework**: [Next.js](https://nextjs.org/) 14 App Router with Server Actions
- **AI**: [OpenAI - GPT 3.5 Turbo](https://openai.com) with [Vercel AI SDK](https://sdk.vercel.ai)
- **Database**: [Supabase](https://supabase.com/) 
- **Authentication**: [Clerk](https://clerk.com/) 
- **Deployment**: [Vercel](https://vercel.com/)
- **Analytics**: [Vercel Analytics](https://vercel.com/analytics/)
- [Zod](https://zod.dev/) for TypeScript-first schema declaration and validation  
- Automatic import sorting with `@ianvs/prettier-plugin-sort-imports`

## Running Locally

1. Clone the repository and install the dependencies

```bash
pnpm install
```

2. Copy the `.env.example` to `.env` and update the variables.

```bash
copy .env.example .env
```

3. Start the development server

```bash
pnpm run dev
```


