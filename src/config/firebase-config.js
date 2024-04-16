// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAWgk26VIO3ICpsFKW3BqqmBHoRcJAZgok",
  authDomain: "expense-tracker-e0ced.firebaseapp.com",
  projectId: "expense-tracker-e0ced",
  storageBucket: "expense-tracker-e0ced.appspot.com",
  messagingSenderId: "798466450069",
  appId: "1:798466450069:web:d3fe9081b059f1f917319c",
  measurementId: "G-LTT96J92N3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);