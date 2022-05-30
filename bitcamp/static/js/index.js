gsap.from('.header', { duration: 1, y: '-100%', ease: 'bounce.out' })

gsap.from('.main-nav-item', {
  y: '-100%',
  duration: 0.1,
  opacity: 0,
  delay: 0.3,
  stagger: 0.1,
})

gsap.from('.footer-nav-item', {
  scrollTrigger: '.footer',
  duration: 0.3,
  y: '-100%',
  opacity: 0,

  stagger: 0.2,
})
