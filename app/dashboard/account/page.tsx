import type { Metadata } from "next"

import { UserProfile } from "@/components/dashboard/user-profile"

export const metadata: Metadata = {
    // for deployment and changeable 
  metadataBase: new URL("https://gastrono-genuis.app"),
  title: "Account",
  description: "Manage your account settings",
}

export default function AccountPage() {
  return (
    <div className="w-full overflow-hidden">
      <UserProfile />
    </div>
  )
}
