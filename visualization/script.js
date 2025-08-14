const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const resize = () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight }
resize()
window.addEventListener('resize', resize)
const draw = data => {
  ctx.clearRect(0,0,canvas.width,canvas.height)
  data.synapses.forEach(s => {
    const a = data.neurons.find(n => n.id === s.pre)
    const b = data.neurons.find(n => n.id === s.post)
    ctx.beginPath()
    ctx.moveTo(a.position[0]*100+canvas.width/2, a.position[1]*100+canvas.height/2)
    ctx.lineTo(b.position[0]*100+canvas.width/2, b.position[1]*100+canvas.height/2)
    ctx.stroke()
  })
  data.nmjs.forEach(j => {
    const n = data.neurons.find(x => x.id === j.neuron)
    ctx.beginPath()
    ctx.moveTo(n.position[0]*100+canvas.width/2, n.position[1]*100+canvas.height/2)
    ctx.lineTo(n.position[0]*100+canvas.width/2, n.position[1]*100+canvas.height/2+20)
    ctx.strokeStyle = 'red'
    ctx.stroke()
    ctx.strokeStyle = 'black'
  })
  data.neurons.forEach(n => {
    ctx.beginPath()
    ctx.arc(n.position[0]*100+canvas.width/2, n.position[1]*100+canvas.height/2, 10, 0, Math.PI*2)
    ctx.fill()
  })
}
fetch('../data/network.json').then(r => r.json()).then(draw)
