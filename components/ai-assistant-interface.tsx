"use client"

import type React from "react"
import { useState } from "react"
import { Send, Plus, MessageSquare } from "lucide-react"

export default function AIAssistantInterface() {
  const [messages, setMessages] = useState([{ text: "Hello! How can I assist you today?", isBot: true }])
  const [input, setInput] = useState("")

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim()) {
      setMessages([...messages, { text: input, isBot: false }])
      setInput("")
      
      try {
        const response = await fetch('http://localhost:8000/api/chat', { // UPDATED URL
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: input }),
        });
        
        const data = await response.json();
        setMessages((prev) => [...prev, { text: data.response, isBot: true }]);
      } catch (error) {
        setMessages((prev) => [...prev, { text: "Sorry, I'm having trouble connecting to the server.", isBot: true }]);
      }
    }
  }

  const startNewChat = () => {
    setMessages([{ text: "Hello! How can I assist you today?", isBot: true }])
  }

  const conversationStarters = [
    "Tell me about the latest AI advancements",
    "How can AI improve productivity?",
    "Explain quantum computing in simple terms",
  ]

  return (
    <div className="flex h-screen bg-[#E2E8C0] text-[#443742]">
      {/* Sidebar */}
      <div className="w-64 bg-[#CEA07E] border-r border-[#846C5B] p-4 flex flex-col">
        <button
          onClick={startNewChat}
          className="flex items-center justify-center w-full p-2 mb-4 bg-[#443742] text-[#E2E8C0]"
        >
          <Plus size={18} className="mr-2" /> New Chat
        </button>
        <div className="flex-1 overflow-y-auto">
          {conversationStarters.map((starter, index) => (
            <button
              key={index}
              className="flex items-center w-full p-2 mb-2 text-left bg-[#EDD9A3] text-[#443742] hover:bg-[#846C5B] hover:text-[#E2E8C0]"
              onClick={() => setInput(starter)}
            >
              <MessageSquare size={18} className="mr-2 flex-shrink-0" />
              <span className="truncate">{starter}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Chat Interface */}
      <div className="flex-1 flex flex-col max-w-3xl">
        <header className="p-2 bg-[#443742] text-[#E2E8C0]">
          <h1 className="text-lg font-bold">AI Assistant</h1>
        </header>
        <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-[#E2E8C0]">
          {messages.map((message, index) => (
            <div key={index} className={`flex ${message.isBot ? "justify-start" : "justify-end"}`}>
              <div
                className={`p-2 max-w-[70%] ${message.isBot ? "bg-[#846C5B] text-[#E2E8C0]" : "bg-[#EDD9A3] text-[#443742]"}`}
              >
                {message.text}
              </div>
            </div>
          ))}
        </div>
        <form onSubmit={handleSend} className="p-2 bg-[#CEA07E] flex">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 p-2 bg-[#EDD9A3] text-[#443742] placeholder-[#846C5B] outline-none"
          />
          <button type="submit" className="ml-2 p-2 bg-[#443742] text-[#E2E8C0]">
            <Send size={20} />
          </button>
        </form>
      </div>
    </div>
  )
}

