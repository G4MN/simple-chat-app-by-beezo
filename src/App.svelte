<script>
	import { onMount, afterUpdate } from 'svelte';
	let messagesContainer;
	let message = "";
	let messages = [];
	let ws;
	let name = "Anonymous";
	let connectionStatus = "Connecting...";

	function connect() {
	ws = new WebSocket("ws://" + location.hostname + ":8000/ws");

	ws.onmessage = (event) => {
	messages = [...messages, event.data];
	};

	ws.onopen = () => {
	connectionStatus = "Connected";
	ws.send(`${name} joined the chat.`);
	};

	ws.onclose = () => {
	connectionStatus = "Disconnected";
	setTimeout(connect, 1000);
	};
	}

	connect();

	function sendMessage() {
	ws.send(`${name}: ${message}`);
	message = "";
	}

	onMount(() => {
	scrollToBottom();
	});

	afterUpdate(() => {
	scrollToBottom();
	});

	function scrollToBottom() {
	if (messagesContainer) {
	messagesContainer.scrollTop = messagesContainer.scrollHeight;
	}
	}
</script>

<main>
	<div class="container">
		<div class="chat-window">
			<div class="header">
				<h1>Simple Chat</h1>
			</div>
			<div class="messages" bind:this="{messagesContainer}">
				{#each messages.slice().reverse() as msg}
				<div class="message">{msg}</div>
				{/each}
			</div>
			<div class="input-area">
				<input bind:value="{message}" class="input" placeholder="Type a message" />
				<button on:click="{sendMessage}" class="send-button">Send</button>
			</div>
			<div class="status">Connection status: {connectionStatus}</div>
		</div>
	</div>
</main>

<style>
	* {
	box-sizing: border-box;
	margin: 0;
	padding: 0;
	}

	body {
	background-color: #1e1e1e;
	font-family: Arial, sans-serif;
	display: flex;
	flex-direction: column;
	}

	main {
	flex-grow: 1;
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 1rem;
	}

	.container {
	width: 100%;
	max-width: 800px;
	display: flex;
	flex-direction: column;
	height: 100%;
	}

	.header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 1rem;
	color: #fff;
	}

	.chat-window {
	width: 100%;
	height: 100%;
	background-color: #2c2c2c;
	border-radius: 8px;
	padding: 1rem;
	display: flex;
	flex-direction: column;
	}

	.messages {
	flex-grow: 1;
	overflow-y: scroll;
	margin-bottom: 1rem;
	padding: 0.5rem;
	background-color: #3c3c3c;
	border-radius: 4px;
	min-height: calc(80vh - 140px);
	max-height: calc(80vh - 140px);
	display: flex;
	flex-direction: column-reverse;
	}

	.message {
	color: #fff;
	margin-bottom: 0.5rem;
	padding: 0.5rem;
	}

	.input-area {
	display: flex;
	}

	.input {
	flex-grow: 1;
	border: 1px solid #666;
	border-radius: 4px;
	padding: 0.5rem;
	margin-right: 0.5rem;
	color: #fff;
	background-color: #444;
	}

	.send-button {
	background-color: #007bff;
	border: none;
	border-radius: 4px;
	color: #ffffff;
	font-size: 1rem;
	padding: 0.5rem 1rem;
	cursor: pointer;
	}

	.status {
	color: #ccc;
	font-size: 0.9rem;
	margin-top: 1rem;
	text-align: center;
	}

	/* Style for the scrollbar */
	.messages::-webkit-scrollbar {
	width: 6px;
	}

	.messages::-webkit-scrollbar-track {
	background-color: #1e1e1e;
	}

	.messages::-webkit-scrollbar-thumb {
	background-color: #666;
	border-radius: 4px;
	}

	/* Responsive design */
	@media (max-width: 767px) {
	.container {
	max-width: 100%;
	}
	}
</style>