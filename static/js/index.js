const socketio = io()

socketio.on("connect", () => {
  console.log("on connected")
})

socketio.on("response", (message) => {
  document.getElementById("counter").innerHTML = message.data
})

socketio.on("counter", () => {
  console.log(`start count`)
})
