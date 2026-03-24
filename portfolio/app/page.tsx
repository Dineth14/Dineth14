import { About } from '@/components/About';
import { Contact } from '@/components/Contact';
import { Footer } from '@/components/Footer';
import { GitHubStats } from '@/components/GitHubStats';
import { Hero } from '@/components/Hero';
import { Navbar } from '@/components/Navbar';
import { Projects } from '@/components/Projects';
import { Research } from '@/components/Research';
import { TechStack } from '@/components/TechStack';

export default function Home() {
  return (
    <>
      <Navbar />
      <main className='relative overflow-x-clip'>
        <Hero />
        <About />
        <Research />
        <Projects />
        <TechStack />
        <GitHubStats />
        <Contact />
      </main>
      <Footer />
    </>
  );
}
