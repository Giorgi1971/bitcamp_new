gsap.fromTo(
  '.single-post',
  {
    y: 300,
    opacity: 0,
  },
  {
    y: 0,
    opacity: 1,
    duration: 1,
    ease: 'power4.out',
  }
)
gsap.from('.single-category', {
  opacity: 0,
  duration: 0.5,
  stagger: 0.3,
  x: 100,
  ease: 'power4.out',
})
