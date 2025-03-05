import { useState } from "react";
import "./chat.css";
import Navbar from "../../navbar/navbar.jsx";

function Chat() {
	const [messages, setMessages] = useState([]);
	const [input, setInput] = useState("");

	const handleSendMessage = () => {
		if (input.trim() === "") return;

		const newMessage = { text: input, sender: "user" };
		setMessages([...messages, newMessage]);
		setInput("");

		setTimeout(() => {
			const aiMessage = { text: `AI response to: ${input}`, sender: "ai" };
			setMessages((prevMessages) => [...prevMessages, aiMessage]);
		}, 1000);
	};

	return (
		<>
			<Navbar />
			<div className="chat-container">
				<div className="messages-container">
					{messages.map((message, index) => (
						<div
							key={index}
							className={`message ${
								message.sender === "user"
									? "user-message"
									: "ai-message"
							}`}
						>
							{message.text}
						</div>
					))}
				</div>
				<div className="input-container">
					<input
						type="text"
						value={input}
						onChange={(e) => setInput(e.target.value)}
						className="input-field"
						placeholder="Type your message..."
					/>
					<button onClick={handleSendMessage} className="send-button">
						Send
					</button>
				</div>
			</div>
		</>
	);
}

export default Chat;
