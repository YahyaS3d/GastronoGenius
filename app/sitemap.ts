import { MetadataRoute } from "next"

export default function sitemap(): MetadataRoute.Sitemap {
        //deployment and changeable 
  const baseUrl = "https://gastrono-genuis.app"
  return [
    {
      url: baseUrl,
      lastModified: new Date(),
    },
  ]
}
