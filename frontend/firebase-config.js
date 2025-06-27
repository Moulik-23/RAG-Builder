// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.9.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.9.1/firebase-analytics.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/11.9.1/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBFCuZsJ8D81Z8Dd0eK2WL-6tQtvGTy61Q",
  authDomain: "rag-builder-530e0.firebaseapp.com",
  projectId: "rag-builder-530e0",
  storageBucket: "rag-builder-530e0.firebasestorage.app",
  messagingSenderId: "297329401187",
  appId: "1:297329401187:web:9bc6087fab17bc12a58756",
  measurementId: "G-9KFEYEG5T4",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const submit = document.getElementById("submit");
submit.addEventListener("click", function (event) {
  event.preventDefault();
  
  const email = document.getElementById('email').value;
  const password = document.getElementById('Password').value;
  const auth = getAuth();
  createUserWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      // Signed up
      const user = userCredential.user;
      
      window.location.href = 'index.html'
      // ...
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage);
      // ..
    });
});
