'use client';

import { motion } from 'framer-motion';
import { ArrowUpRight, Lock, Microscope } from 'lucide-react';
import { fadeUp, staggerParent } from '@/lib/animations';
import { projects } from '@/lib/site-data';
import { GlowCard } from './ui/GlowCard';

export function Projects() {
  return (
    <section id='projects' className='relative border-b border-white/5 py-24 sm:py-28'>
      <div className='section-shell'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.18 }}
          variants={staggerParent}
          className='space-y-12'
        >
          <motion.div variants={fadeUp} className='space-y-5'>
            <span className='section-kicker'>Active Research Projects</span>
            <h2 className='max-w-4xl font-display text-4xl leading-tight text-mist sm:text-5xl'>
              Lab-bench builds spanning Mamba architectures, embedded sensing, and
              physically constrained group reasoning.
            </h2>
          </motion.div>

          <motion.div
            variants={staggerParent}
            className='-mx-4 flex snap-x gap-5 overflow-x-auto px-4 pb-3 md:mx-0 md:grid md:grid-cols-3 md:overflow-visible md:px-0'
          >
            {projects.map((project) => {
              const isPrivate = !project.href;
              const accentClasses =
                project.accent === 'ember'
                  ? 'border-ember/35 shadow-[0_0_0_1px_rgba(255,107,53,0.18)]'
                  : 'border-cyan/35 shadow-[0_0_0_1px_rgba(0,231,255,0.16)]';

              return (
                <motion.div
                  key={project.title}
                  variants={fadeUp}
                  className='min-w-[86vw] snap-center md:min-w-0'
                >
                  <GlowCard className='group h-full rounded-[1.8rem] p-6 transition duration-300 hover:-translate-y-1 sm:p-7'>
                    <div
                      className={`mb-6 h-1 w-full rounded-full ${
                        project.accent === 'ember' ? 'bg-ember/90' : 'bg-cyan/90'
                      }`}
                    />
                    <div className='flex h-full flex-col'>
                      <div className='mb-5 flex items-center justify-between gap-4'>
                        <span
                          className={`inline-flex items-center gap-2 rounded-full border px-3 py-1 text-[0.7rem] uppercase tracking-[0.2em] ${accentClasses}`}
                        >
                          <Microscope className='h-3.5 w-3.5' />
                          {project.status === 'COMPLETE' ? 'Complete' : 'In Progress'}
                        </span>
                        <span className='text-[0.68rem] uppercase tracking-[0.25em] text-mist/38'>
                          Lab Node
                        </span>
                      </div>

                      <h3 className='font-mono text-2xl leading-tight text-mist'>
                        {project.title}
                      </h3>
                      <p className='mt-5 flex-1 text-sm leading-7 text-mist/72'>
                        {project.description}
                      </p>

                      <div className='mt-6 flex flex-wrap gap-2'>
                        {project.tags.map((tag) => (
                          <span
                            key={tag}
                            className='rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[0.68rem] uppercase tracking-[0.18em] text-mist/70'
                          >
                            {tag}
                          </span>
                        ))}
                      </div>

                      {isPrivate ? (
                        <div className='mt-8 inline-flex items-center gap-3 rounded-full border border-white/10 bg-white/5 px-4 py-3 text-[0.76rem] uppercase tracking-[0.18em] text-mist/62'>
                          <Lock className='h-4 w-4 text-cyan' />
                          {project.cta}
                        </div>
                      ) : (
                        <a
                          href={project.href}
                          target='_blank'
                          rel='noreferrer'
                          className='mt-8 inline-flex items-center gap-3 rounded-full border border-cyan/25 bg-cyan/8 px-4 py-3 text-[0.76rem] uppercase tracking-[0.18em] text-cyan transition hover:border-cyan/60 hover:bg-cyan/14'
                        >
                          {project.cta}
                          <ArrowUpRight className='h-4 w-4' />
                        </a>
                      )}
                    </div>
                  </GlowCard>
                </motion.div>
              );
            })}
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
