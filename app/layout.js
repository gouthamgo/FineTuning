import './globals.css'

export const metadata = {
  title: 'Fine-Tuning Academy - Learn AI Like a Friend',
  description: 'Learn to fine-tune AI models from scratch. Free, interactive, and actually fun!',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
