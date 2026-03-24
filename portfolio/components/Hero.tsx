'use client';

import dynamic from 'next/dynamic';
import { motion } from 'framer-motion';
import { ArrowDown, ArrowRight, Github } from 'lucide-react';
import { useEffect, useState } from 'react';
import { typewriterLines } from '@/lib/site-data';
import { AnimatedText } from './ui/AnimatedText';
import { RadarSweep } from './ui/RadarSweep';

const SignalScene = dynamic(() => import('./ui/SignalScene'), {
  ssr: false,
});

function useTypewriter(lines: readonly string[]) {
  const [lineIndex, setLineIndex] = useState(0);
  const [displayed, setDisplayed] = useState('');
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    const currentLine = lines[lineIndex];
    const complete = displayed === currentLine;
    const empty = displayed.length === 0;

    const timeout = window.setTimeout(
      () => {
        if (!deleting && !complete) {
          setDisplayed(currentLine.slice(0, displayed.length + 1));
          return;
        }

        if (!deleting && complete) {
          setDeleting(true);
          return;
        }

        if (deleting && !empty) {
          setDisplayed(currentLine.slice(0, displayed.length - 1));
          return;
        }

        setDeleting(false);
        setLineIndex((current) => (current + 1) % lines.length);
      },
      !deleting && complete ? 1800 : deleting ? 35 : 55,
    );

    return () => window.clearTimeout(timeout);
  }, [deleting, displayed, lineIndex, lines]);

  return displayed;
}

export function Hero() {
  const typewriterText = useTypewriter(typewriterLines);
  const [showScene, setShowScene] = useState(false);

  useEffect(() => {
    const media = window.matchMedia('(min-width: 1024px)');
    const sync = () => setShowScene(media.matches);

    sync();
    media.addEventListener('change', sync);
    return () => media.removeEventListener('change', sync);
  }, []);

  return (
    <section
      id='home'
      className='relative flex min-h-screen items-center overflow-hidden border-b border-white/5 pb-16 pt-10'
    >
      <div className='hero-mesh' />
      <div className='noise-dot' />
      {showScene ? <SignalScene /> : null}

      <div className='absolute inset-x-0 top-[16%] z-0 hidden h-[380px] opacity-50 lg:block'>
        <svg
          viewBox='0 0 1200 380'
          className='oscilloscope-line h-full w-full'
          fill='none'
          aria-hidden='true'
        >
          <path
            d='M0 225C60 225 60 170 120 170C180 170 180 245 240 245C300 245 300 125 360 125C420 125 420 260 480 260C540 260 540 110 600 110C660 110 660 232 720 232C780 232 780 168 840 168C900 168 900 264 960 264C1020 264 1020 188 1080 188C1140 188 1140 225 1200 225'
            stroke='rgba(0, 231, 255, 0.9)'
            strokeWidth='2.5'
            strokeLinecap='round'
          />
        </svg>
      </div>

      <div className='section-shell relative z-10 grid gap-14 py-20 lg:grid-cols-[minmax(0,1fr)_340px] lg:items-center'>
        <motion.div
          initial='hidden'
          animate='visible'
          variants={{
            hidden: {},
            visible: {
              transition: {
                staggerChildren: 0.14,
                delayChildren: 0.08,
              },
            },
          }}
          className='max-w-4xl'
        >
          <motion.div
            variants={{
              hidden: { opacity: 0, y: 20 },
              visible: { opacity: 1, y: 0, transition: { duration: 0.55 } },
            }}
            className='mb-6'
          >
            <span className='signal-chip'>
              <span className='dot' />
              Open to Research Collaborations
            </span>
          </motion.div>

          <motion.p
            variants={{
              hidden: { opacity: 0, y: 18 },
              visible: { opacity: 1, y: 0, transition: { duration: 0.55 } },
            }}
            className='mb-5 text-[0.8rem] uppercase tracking-[0.4em] text-cyan/72'
          >
            Electronics Engineer · AI Researcher · Systems Builder
          </motion.p>

          <motion.h1
            variants={{
              hidden: { opacity: 0 },
              visible: { opacity: 1, transition: { duration: 0.2 } },
            }}
            className='max-w-5xl font-display text-[3.15rem] uppercase leading-[0.9] tracking-[0.16em] text-mist sm:text-[4.6rem] lg:text-[6.6rem]'
          >
            <AnimatedText text='DINETH PERERA' />
          </motion.h1>

          <motion.p
            variants={{
              hidden: { opacity: 0, y: 16 },
              visible: { opacity: 1, y: 0, transition: { duration: 0.55, delay: 0.3 } },
            }}
            className='mt-6 max-w-3xl text-base leading-8 text-mist/74 sm:text-lg'
          >
            I build theory-backed systems where embedded constraints, signal fidelity, and
            machine learning elegance all matter at once.
          </motion.p>

          <motion.div
            variants={{
              hidden: { opacity: 0, y: 18 },
              visible: { opacity: 1, y: 0, transition: { duration: 0.55, delay: 0.42 } },
            }}
            className='mt-8 h-8 font-mono text-sm text-ember sm:text-base'
          >
            <span className='text-cyan'>signal://</span> {typewriterText}
            <span className='ml-1 inline-block h-5 w-px animate-pulse bg-ember align-middle' />
          </motion.div>

          <motion.div
            variants={{
              hidden: { opacity: 0, y: 18 },
              visible: { opacity: 1, y: 0, transition: { duration: 0.55, delay: 0.56 } },
            }}
            className='mt-10 flex flex-col gap-4 sm:flex-row'
          >
            <a href='#research' className='signal-button' data-cursor='active'>
              View Research <ArrowRight className='h-4 w-4' />
            </a>
            <a
              href='https://github.com/Dineth14'
              target='_blank'
              rel='noreferrer'
              className='signal-button secondary'
              data-cursor='active'
            >
              GitHub <Github className='h-4 w-4' />
            </a>
          </motion.div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.94, y: 24 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.24, ease: [0.22, 1, 0.36, 1] }}
          className='relative mx-auto hidden w-full max-w-[320px] lg:block'
        >
          <div className='absolute inset-0 rounded-full bg-cyan/10 blur-3xl' />
          <RadarSweep className='w-full' />
          <div className='absolute inset-[15%] rounded-full border border-dashed border-white/10' />
          <div className='absolute inset-x-[24%] top-[28%] rounded-full border border-cyan/16 bg-ink/70 px-4 py-2 text-center text-[0.72rem] uppercase tracking-[0.25em] text-cyan/82'>
            Research Core
          </div>
        </motion.div>
      </div>

      <motion.a
        href='#about'
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.9, duration: 0.45 }}
        className='absolute bottom-8 left-1/2 z-10 inline-flex -translate-x-1/2 items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-[0.68rem] uppercase tracking-[0.28em] text-mist/65'
      >
        Scroll <ArrowDown className='h-3.5 w-3.5 animate-bounce' />
      </motion.a>
    </section>
  );
}
