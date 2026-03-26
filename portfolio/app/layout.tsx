import type { Metadata } from 'next';
import { JetBrains_Mono, Syne } from 'next/font/google';
import './globals.css';
import { CustomCursor } from '@/components/ui/CustomCursor';

const syne = Syne({
  subsets: ['latin'],
  variable: '--font-syne',
  display: 'swap',
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-jetbrains-mono',
  display: 'swap',
});

export const metadata: Metadata = {
  metadataBase: new URL('https://dineth14.github.io'),
  title: 'Dineth Perera | Electronics Engineer & AI Researcher',
  description:
    'Electronics engineering undergraduate focused on embedded AI, remote sensing, Vision Mamba architectures, and group activity recognition.',
  keywords: [
    'electronics engineer',
    'AI researcher',
    'embedded systems',
    'remote sensing',
    'Vision Mamba',
    'Sri Lanka',
  ],
  openGraph: {
    title: 'Dineth Perera - Signal to Intelligence',
    description: 'Electronics Engineer · AI Researcher · Systems Builder',
    url: 'https://dineth14.github.io',
    images: ['/og-image.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Dineth Perera - Signal to Intelligence',
    description: 'Electronics Engineer · AI Researcher · Systems Builder',
    images: ['/og-image.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en' suppressHydrationWarning>
      <body
        className={`${syne.variable} ${jetbrainsMono.variable} bg-ink font-mono text-mist antialiased`}
      >
        <CustomCursor />
        <div className='app-shell'>{children}</div>
      </body>
    </html>
  );
}
