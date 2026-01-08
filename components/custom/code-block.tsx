"use client"

import { Copy, Download, Check } from "lucide-react"
import { Button } from "@/components/ui/button"
import { useState } from "react"
import { cn } from "@/lib/utils"

interface CodeBlockProps {
  code: string
  language?: string
  filename?: string
  className?: string
  showLineNumbers?: boolean
}

export function CodeBlock({ code, language = "python", filename, className, showLineNumbers = false }: CodeBlockProps) {
  const [copied, setCopied] = useState(false)

  const handleCopy = async () => {
    await navigator.clipboard.writeText(code)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const handleDownload = () => {
    const element = document.createElement("a")
    const ext = language === "python" ? "py" : language
    const name = filename || `code.${ext}`
    element.setAttribute("href", `data:text/plain;charset=utf-8,${encodeURIComponent(code)}`)
    element.setAttribute("download", name)
    element.style.display = "none"
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)
  }

  return (
    <div className={cn("rounded-lg border overflow-hidden bg-muted", className)}>
      {/* Header */}
      {filename && (
        <div className="flex items-center justify-between px-4 py-3 border-b bg-card">
          <span className="text-sm font-medium">{filename}</span>
          <div className="flex gap-2">
            <Button variant="ghost" size="sm" onClick={handleCopy} className="gap-2 h-8 px-2">
              {copied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
              <span className="text-xs">{copied ? "Copied" : "Copy"}</span>
            </Button>
            <Button variant="ghost" size="sm" onClick={handleDownload} className="gap-2 h-8 px-2">
              <Download className="w-4 h-4" />
              <span className="text-xs">Download</span>
            </Button>
          </div>
        </div>
      )}

      {/* Code */}
      <pre className="p-4 overflow-x-auto">
        <code className={`language-${language} text-sm leading-relaxed`}>
          {showLineNumbers
            ? code
                .split("\n")
                .map((line, i) => `${String(i + 1).padStart(3, " ")} | ${line}`)
                .join("\n")
            : code}
        </code>
      </pre>
    </div>
  )
}
