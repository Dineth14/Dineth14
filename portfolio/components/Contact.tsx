'use client';

import { motion } from 'framer-motion';
import { ArrowRight, Github, Linkedin, Mail, MapPin } from 'lucide-react';
import { fadeUp, staggerParent } from '@/lib/animations';
import { GlowCard } from './ui/GlowCard';

export function Contact() {
  return (
    <section id='contact' className='relative overflow-hidden py-24 sm:py-28'>
      <div className='contact-waves' />
      <div className='section-shell relative z-10'>
        <motion.div
          initial='hidden'
          whileInView='visible'
          viewport={{ once: true, amount: 0.2 }}
          variants={staggerParent}
          className='space-y-10'
        >
          <motion.div variants={fadeUp} className='space-y-5'>
            <span className='section-kicker'>Contact</span>
            <h2 className='max-w-4xl font-display text-4xl leading-tight text-mist sm:text-5xl lg:text-6xl'>
              LET&apos;S BUILD SOMETHING REAL
            </h2>
            <p className='max-w-3xl text-base leading-8 text-mist/72 sm:text-lg'>
              Open to research collaborations, internships, and embedded AI projects.
            </p>
          </motion.div>

          <motion.div
            variants={staggerParent}
            className='grid gap-6 lg:grid-cols-[minmax(0,1.2fr)_320px]'
          >
            <motion.div variants={fadeUp}>
              <GlowCard className='rounded-[2rem] p-7 sm:p-8'>
                <div className='flex flex-col gap-4 sm:flex-row'>
                  <a href='mailto:dp18perera@gmail.com' className='signal-button flex-1 justify-center'>
                    Send Email <ArrowRight className='h-4 w-4' />
                  </a>
                  <a
                    href='https://github.com/Dineth14'
                    target='_blank'
                    rel='noreferrer'
                    className='signal-button secondary flex-1 justify-center'
                  >
                    View GitHub <Github className='h-4 w-4' />
                  </a>
                </div>

                <div className='mt-8 grid gap-4 md:grid-cols-2'>
                  <a
                    href='mailto:dp18perera@gmail.com'
                    className='rounded-[1.4rem] border border-white/8 bg-white/5 p-5 transition hover:border-cyan/28'
                  >
                    <div className='mb-3 flex items-center gap-3 text-cyan'>
                      <Mail className='h-5 w-5' />
                      <span className='text-[0.72rem] uppercase tracking-[0.22em] text-cyan/78'>
                        Email
                      </span>
                    </div>
                    <p className='text-lg text-mist'>dp18perera@gmail.com</p>
                  </a>

                  <a
                    href='https://www.linkedin.com/in/dineth-perera-ba9657277/'
                    target='_blank'
                    rel='noreferrer'
                    className='rounded-[1.4rem] border border-white/8 bg-white/5 p-5 transition hover:border-ember/28'
                  >
                    <div className='mb-3 flex items-center gap-3 text-ember'>
                      <Linkedin className='h-5 w-5' />
                      <span className='text-[0.72rem] uppercase tracking-[0.22em] text-ember/78'>
                        LinkedIn
                      </span>
                    </div>
                    <p className='text-lg text-mist'>linkedin.com/in/dineth-perera-ba9657277</p>
                  </a>
                </div>
              </GlowCard>
            </motion.div>

            <motion.div variants={fadeUp}>
              <GlowCard className='h-full rounded-[2rem] p-7 sm:p-8'>
                <p className='text-[0.72rem] uppercase tracking-[0.28em] text-cyan/78'>
                  Field Node
                </p>
                <h3 className='mt-4 font-display text-3xl text-mist'>Sri Lanka</h3>
                <p className='mt-4 text-sm leading-7 text-mist/68'>
                  Working at the intersection of embedded intelligence, remote sensing,
                  and vision research from Sri Lanka.
                </p>
                <div className='mt-8 inline-flex items-center gap-3 rounded-full border border-white/10 bg-white/5 px-4 py-3 text-[0.74rem] uppercase tracking-[0.22em] text-mist/72'>
                  <MapPin className='h-4 w-4 text-ember' />
                  Sri Lanka
                </div>
              </GlowCard>
            </motion.div>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
