var CACHE_NAME = "Task_Cache";
var urlsToCache = [
  "/",
];

self.addEventListener("install", function (event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      console.log("Opened cache");
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return fetch(event.request).catch(function (rsp) {
        return response;
      });
    })
  );
});

//solo para cachear todo reemplazar por esta versión del Fetch

self.addEventListener("fetch", function (event) {
  event.respondWith(
    fetch(event.request)
      .then((result) => {
        return caches.open(CACHE_NAME).then(function (c) {
          c.put(event.request.url, result.clone());
          return result;
        });
      })
      .catch(function (e) {
        return caches.match(event.request);
      })
  );
});



//Codigo para notificaciones push
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');




var firebaseConfig = {
  apiKey: "AIzaSyDrD2mK5SWzhnE5jbQGjUNLDTXtRJ1knNI",
  authDomain: "task-manager-61af9.firebaseapp.com",
  databaseURL: "https://task-manager-61af9.firebaseio.com",
  projectId: "task-manager-61af9",
  storageBucket: "task-manager-61af9.appspot.com",
  messagingSenderId: "968347017557",
  appId: "1:968347017557:web:d4d1e83373864fff238fdc"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);


let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
      let title = payload.notification.title;
      let options = {
        body:payload.notification.body,
        icon:payload.notification.icon
      }

      self.registration.showNotification(title, options)
})

