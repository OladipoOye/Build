import { Provider } from "@/components/ui/provider"
import Navigation from "./components/navigation"

export default function RootLayout(props) {
  const { children } = props
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