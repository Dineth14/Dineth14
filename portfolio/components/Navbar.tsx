'use client';

import { motion } from 'framer-motion';
import { Github, Orbit } from 'lucide-react';
import { useEffect, useState } from 'react';
import { navSections } from '@/lib/site-data';

export function Navbar() {
  const [active, setActive] = useState('home');
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const sections = navSections
      .map((section) => document.getElementById(section.id))
      .filter(Boolean) as HTMLElement[];

    const observer = new IntersectionObserver(
      (entries) => {
        const visibleEntry = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];

        if (visibleEntry?.target.id) {
          setActive(visibleEntry.target.id);
        }
      },
      {
        threshold: [0.25, 0.45, 0.7],
        rootMargin: '-20% 0px -45% 0px',
      },
    );

    sections.forEach((section) => observer.observe(section));

    const handleScroll = () => {
      setVisible(window.scrollY > window.innerHeight * 0.45);
    };

    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });

    return () => {
      window.removeEventListener('scroll', handleScroll);
      observer.disconnect();
    };
  }, []);

  const scrollToSection = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  return (
    <motion.nav
      initial={{ opacity: 0, y: -24 }}
      animate={{
        opacity: visible ? 1 : 0,
        y: visible ? 0 : -24,
        pointerEvents: visible ? 'auto' : 'none',
      }}
      transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
      className='fixed inset-x-0 top-4 z-40'
    >
      <div className='section-shell'>
        <div className='glass-nav flex items-center justify-between gap-4 rounded-full px-4 py-3 md:px-6'>
          <button
            type='button'
            onClick={() => scrollToSection('home')}
            className='flex items-center gap-3 text-left'
          >
            <span className='rounded-full border border-cyan/20 bg-cyan/10 p-2 text-cyan'>
              <Orbit className='h-4 w-4' />
            </span>
            <span className='font-display text-sm uppercase tracking-[0.36em] text-white/90'>
              Dineth Perera
            </span>
          </button>

          <div className='hidden items-center gap-2 lg:flex'>
            {navSections.map((section) => {
              const current = active === section.id;

              return (
                <button
                  key={section.id}
                  type='button'
                  onClick={() => scrollToSection(section.id)}
                  className={`rounded-full px-4 py-2 text-[0.72rem] uppercase tracking-[0.22em] transition ${
                    current
                      ? 'bg-cyan/12 text-cyan shadow-[0_0_0_1px_rgba(0,231,255,0.2)]'
                      : 'text-mist/60 hover:text-mist'
                  }`}
                >
                  {section.label}
                </button>
              );
            })}
          </div>

          <a
            href='https://github.com/Dineth14'
            target='_blank'
            rel='noreferrer'
            className='inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-2 text-[0.72rem] uppercase tracking-[0.22em] text-mist/80 transition hover:border-cyan/30 hover:text-cyan'
          >
            <Github className='h-4 w-4' />
            GitHub
          </a>
        </div>
      </div>
    </motion.nav>
  );
}
