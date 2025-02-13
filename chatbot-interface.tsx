"use client"

import type React from "react"
import { useState } from "react"
import { Send } from "lucide-react"

export default function ChatbotInterface() {
  const [messages, setMessages] = useState([
    { text: "Hello! How can I assist you today?", isBot: true },
    { text: "Hi there! I have a question about your services.", isBot: false },
    { text: "Of course! I'd be happy to help. What would you like to know?", isBot: true },
  ])
  const [input, setInput] = useState("")

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim()) {
      setMessages([...messages, { text: input, isBot: false }])
      setInput("")
      // Here you would typically call an API to get the bot's response
      setTimeout(() => {
        setMessages((prev) => [...prev, { text: "This is a sample response from the chatbot.", isBot: true }])
      }, 1000)
    }
  }

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto bg-[#080f0f] text-[#eff2c0]">
      <header className="p-4 bg-[#a52422]">
        <h1 className="text-2xl font-bold">Minimalist Chatbot</h1>
      </header>
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-[#eff2c0]">
        {messages.map((message, index) => (
          <div key={index} className={`flex ${message.isBot ? "justify-start" : "justify-end"}`}>
            <div
              className={`p-2 max-w-[70%] ${message.isBot ? "bg-[#a52422] text-[#eff2c0]" : "bg-[#bea57d] text-[#080f0f]"}`}
            >
              {message.text}
            </div>
          </div>
        ))}
      </div>
      <form onSubmit={handleSend} className="p-4 bg-[#080f0f] flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 p-2 bg-[#eff2c0] text-[#080f0f] placeholder-[#a4bab7] outline-none"
        />
        <button type="submit" className="ml-2 p-2 bg-[#a52422] text-[#eff2c0]">
          <Send size={24} />
        </button>
      </form>
    </div>
  )
}

