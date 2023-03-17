import App from "./App.svelte";
import Register from "./Register.svelte";

const routes = [
    { path: "/", component: App },
    { path: "/register", component: Register },
];

export default routes;