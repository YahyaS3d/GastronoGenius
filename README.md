# Gastrono Genius

Clever and creative abilities of GPT generator build from scratch: Creating a compact GPT model tailored for the culinary domain and designed to offer various services.


## Features

- **Framework**: [Next.js](https://nextjs.org/) 14 App Router with Server Actions
- **AI**: [OpenAI - GPT 3.5 Turbo](https://openai.com) with [Vercel AI SDK](https://sdk.vercel.ai)
- **Database**: [Supabase](https://supabase.com/)
- **Authentication**: [Clerk](https://clerk.com/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
  - **Primitives**: [Radix UI](https://radix-ui.com/)
  - **Components**: [shadcn/ui](https://ui.shadcn.com/)
  - **Icons**: [Lucide](https://lucide.dev/)
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


