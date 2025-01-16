import "./globals.css";

import { Provider } from "@/components/ui/provider"
import Navigation from "/components/navigation"

export default function RootLayout({children}) {
  "use client"
  return (
    <html suppressHydrationWarning>
      <body>
        <Provider>
          <Navigation />
          {children}
        </Provider>
      </body>
    </html>
  )
}
