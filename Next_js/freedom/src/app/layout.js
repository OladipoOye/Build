import { ChakraProvider } from "@chakra-ui/react"
import Navigation from "./components/navigation"

export default function RootLayout({children}) {
  return (
    <html suppressHydrationWarning>
      <body>
        <ChakraProvider>
          <Navigation />
          {children}
        </ChakraProvider>
      </body>
    </html>
  )
};
