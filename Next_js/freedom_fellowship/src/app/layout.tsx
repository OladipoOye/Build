//import type { Metadata } from "next";
//import { Geist, Geist_Mono } from "next/font/google";
//import "./globals.css";
// app/layout.tsx
import { Providers } from './providers'
import Navigation from "./components/navigation";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode,
}) {
  return (
    <html lang='en'>
      <body>
        <Navigation />
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}