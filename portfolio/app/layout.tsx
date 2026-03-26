import type { Metadata } from 'next';
import { Sora, Inter, JetBrains_Mono } from 'next/font/google';
import './globals.css';

const sora = Sora({
  subsets: ['latin'],
  variable: '--font-sora',
  display: 'swap',
  weight: ['500', '600'],
});

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
  weight: ['400', '500'],
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-jetbrains-mono',
  display: 'swap',
  weight: ['400'],
});

export const metadata: Metadata = {
  metadataBase: new URL('https://dinethnethsara.vercel.app'),
  title: 'Dineth Nethsara | Researcher · Engineer · Founder',
  description:
    'Electronics & Electrical Engineering undergraduate at University of Peradeniya. Researching Visual State Space Models for remote sensing. Building systems that learn to see.',
  keywords: [
    'electronics engineer',
    'AI researcher',
    'remote sensing',
    'Vision Mamba',
    'state space models',
    'University of Peradeniya',
    'Sri Lanka',
  ],
  openGraph: {
    title: 'Dineth Nethsara — Researcher · Engineer · Founder',
    description:
      'I build systems that learn to see. Researcher. Engineer. Founder.',
    url: 'https://dinethnethsara.vercel.app',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Dineth Nethsara — Researcher · Engineer · Founder',
    description:
      'I build systems that learn to see. Researcher. Engineer. Founder.',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${sora.variable} ${inter.variable} ${jetbrainsMono.variable} bg-deep font-body text-body text-text-primary antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
