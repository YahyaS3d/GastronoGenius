import { NextResponse } from "next/server"
import { authMiddleware } from "@clerk/nextjs"
import { supabaseClient } from "@/lib/supabase-client"

// Next.js application using Clerk for authentication
export default authMiddleware({
  publicRoutes: [
    "/",
    "/sign-in(.*)",
    "/sign-up(.*)",
    "/dashboard(.*)",
    "/dashboard",
    "/sign-out",
    "/api(.*)",
    "/recipes(.*)",
  ],
  async afterAuth(auth, req) {
    if (auth.isPublicRoute) {
      // For public routes, we don't need to do anything
      return NextResponse.next()
    }

    const url = new URL(req.nextUrl.origin)

    if (!auth.userId) {
      // If user tries to access a private route without being authenticated,
      // redirect them to the sign-in page
      url.pathname = "/sign-in"
      return NextResponse.redirect(url)
    }

    // Fetch user details to check role
    const supabase = await supabaseClient(auth.sessionId) // Assuming the sessionId is used as the token
    const { data: user, error } = await supabase
      .from("users")
      .select("role")
      .eq("id", auth.userId)
      .single()

    if (error || !user) {
      // Handle error or if user is not found
      console.error("Error fetching user details:", error)
      url.pathname = "/error"
      return NextResponse.redirect(url)
    }

    if (user.role !== 'admin') {
      // If user is not an admin, redirect to not authorized page
      url.pathname = "/not-authorized"
      return NextResponse.redirect(url)
    }

    return NextResponse.next()
  },
})

export const config = {
  matcher: ["/((?!.*\\..*|_next).*)", "/", "/(api|trpc)(.*)"],
}
