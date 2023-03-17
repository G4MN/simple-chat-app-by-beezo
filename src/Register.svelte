<script>
	import { Link } from "svelte-routing";
	import { onMount } from "svelte";
	let username = "";

	async function register() {
	const response = await fetch("http://localhost:7779/register", {
	method: "POST",
	headers: {
	"Content-Type": "application/json",
	},
	body: JSON.stringify({ username }),
	});

	if (response.ok) {
	localStorage.setItem("username", username);
	window.location.href = "/";
	} else {
	alert("Username already exists");
	}
	}
</script>

<main>
	<h1>Register</h1>
	<div>
		<label for="username">Username:</label>
		<input type="text" bind:value="{username}" />
	</div>
	<button on:click="{register}">Register</button>
</main>

<style>
	main {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
	}
</style>