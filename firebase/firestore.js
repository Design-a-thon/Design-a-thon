import { app } from "./firebase-config.js";

import {
    getFirestore,
    doc,
    setDoc,
    getDoc
} from "https://www.gstatic.com/firebasejs/12.0.0/firebase-firestore.js";

export const db = getFirestore(app);

export {
    doc,
    setDoc,
    getDoc
};