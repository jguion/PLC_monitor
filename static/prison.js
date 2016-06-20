// Subscribe once swampdragon is connected
swampdragon.open(function () {
    swampdragon.subscribe('cell_doors', 'cell_doors');

});

// This is the list of notifications
var doorList = document.getElementById("cell_doors");


// New channel message received
swampdragon.onChannelMessage(function (channels, message) {
    console.log(message);
    // Add the notification
    if (message.action === "created") {
        addDoor((message.data));
    }
    if (message.action === "updated"){
      updateDoor(message.data.id, message.data.secured, message.data.unlocked);
    }
});



function addDoor(door) {
    // If we have permission to show browser notifications
    // we can show the notifiaction
  //  if (window.Notification && Notification.permission === "granted") {
  //      new Notification(notification.message);
  //  }

    // Add the new notification
    var door_div = document.createElement("div");
    $(door_div).attr("id","door"+door.id);
    if (door.secured){
      $(door_div).addClass("door_closed");
      $(door_div).text("Cell "+door.id+ " is closed.");
    }else{
      $(door_div).addClass("door_open")
      $(door_div).text("Cell "+door.id+ " is open!");
    }
    doorList.insertBefore(door_div, doorList.firstChild);
}

function updateDoor(id, secured, unlocked){
  var door = $("#door"+id);
  var past_secured = door.hasClass("door_closed");
  console.log(door);
  if (secured != past_secured){
    door.toggleClass("door_closed door_open")
    if(secured){
      door.text("Cell "+id+" is closed.");
    }else{
      door.text("Cell "+id+" is open!")
    }
  }
}
