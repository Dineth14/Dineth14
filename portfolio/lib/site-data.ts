export const typewriterLines = [
  'Building intelligence from signal to pixel',
  'Hardware-grounded. Algorithm-driven.',
  'Bridging embedded systems & deep learning',
];

export const navSections = [
  { id: 'home', label: 'Home' },
  { id: 'about', label: 'About' },
  { id: 'research', label: 'Research' },
  { id: 'projects', label: 'Projects' },
  { id: 'stack', label: 'Arsenal' },
  { id: 'github', label: 'GitHub' },
  { id: 'contact', label: 'Contact' },
] as const;

export const researchDomains = [
  {
    icon: 'satellite',
    tag: 'Earth Observation',
    title: 'Remote Sensing & Earth Observation',
    bullets: [
      'Bi-temporal & multi-temporal change detection',
      'Semantic segmentation for satellite imagery',
      'Wavelet-domain fusion + edge-aware losses',
    ],
  },
  {
    icon: 'eye',
    tag: 'Vision Systems',
    title: 'Computer Vision & AI',
    bullets: [
      'Vision Mamba / State Space Models for vision',
      'Hybrid CNN-SSM architectures',
      'Lightweight models for edge deployment',
    ],
  },
  {
    icon: 'users',
    tag: 'Behavior Modeling',
    title: 'Group Activity Recognition',
    bullets: [
      'Physically plausible motion constraints',
      'Spatiotemporal graph + transformer models',
      'Action feasibility scoring',
    ],
  },
  {
    icon: 'waveform',
    tag: 'Instrumentation',
    title: 'Signal Processing & Instrumentation',
    bullets: [
      'Real-time embedded audio classification',
      'Noise-aware sensor pipelines',
      'Offline k-NN with ESP32 SPIFFS',
    ],
  },
] as const;

export const projects = [
  {
    status: 'IN PROGRESS',
    accent: 'cyan',
    title: 'Vision Mamba Change Detection',
    description:
      'Designing a hybrid VMamba + CNN dual-stream architecture for bi-temporal remote sensing change detection. Incorporates wavelet-domain feature fusion and edge-aware loss functions for robust urban scene differencing.',
    tags: ['PyTorch', 'VMamba', 'SSM', 'LEVIR-CD', 'WHU-CD'],
    href: null,
    cta: 'Private - Pending Publication',
  },
  {
    status: 'COMPLETE',
    accent: 'ember',
    title: 'ESP32 Real-Time Noise Logger',
    description:
      'Full-stack embedded audio classification system. ESP32 extracts 7D feature vectors (ZCR, RMS, spectral centroid, etc.) via FFT + Hamming window, then classifies with offline k-NN (K=3) from SPIFFS-stored labeled samples. Python GUI for live monitoring.',
    tags: ['C++', 'ESP32', 'Python', 'k-NN', 'DSP', 'SPIFFS'],
    href: 'https://github.com/Dineth14/ESP32-Real-Time-Noise-Logger',
    cta: 'View GitHub',
  },
  {
    status: 'IN PROGRESS',
    accent: 'cyan',
    title: 'GAR with Physical Constraints',
    description:
      'Investigating deep group activity recognition models augmented with physics-aware constraints. Goals: enforce motion consistency and feasibility bounds within spatiotemporal graph networks.',
    tags: ['PyTorch', 'GCN', 'Transformers', 'Volleyball', 'NBA'],
    href: null,
    cta: 'Private - Pending Publication',
  },
] as const;

export const techGroups = [
  {
    title: 'Languages',
    icon: 'code',
    items: ['C', 'C++', 'Python', 'MATLAB'],
  },
  {
    title: 'Deep Learning',
    icon: 'brain',
    items: ['PyTorch', 'TensorFlow', 'OpenCV'],
  },
  {
    title: 'Embedded',
    icon: 'cpu',
    items: ['ESP32', 'Arduino', 'Raspberry Pi', 'AVR'],
  },
  {
    title: 'Tools',
    icon: 'tool',
    items: ['Git', 'Linux', 'Jupyter', 'VS Code'],
  },
  {
    title: 'Research',
    icon: 'orbit',
    items: ['VMamba', 'Mamba', 'Transformers', 'GCNs'],
  },
] as const;

export const githubStats = [
  {
    title: 'Contribution Overview',
    width: 495,
    height: 195,
    src: 'https://github-readme-stats.vercel.app/api?username=Dineth14&show_icons=true&theme=radical&bg_color=0d1117',
  },
  {
    title: 'Current Streak',
    width: 495,
    height: 195,
    src: 'https://github-readme-streak-stats.herokuapp.com?user=Dineth14&theme=radical&background=0d1117',
  },
  {
    title: 'Activity Graph',
    width: 900,
    height: 320,
    src: 'https://github-readme-activity-graph.vercel.app/graph?username=Dineth14&bg_color=0d1117&color=00e7ff&line=00e7ff',
  },
] as const;
