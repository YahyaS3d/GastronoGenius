import { MetadataRoute } from "next"

export default function robots(): MetadataRoute.Robots {
        //deployment and changeable 

  const baseUrl = "https://gastrono-genuis.app"

  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
      },
    ],
    sitemap: `${baseUrl}/sitemap.xml`,
  }
}
