"use client"

import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Toggle } from "@/components/ui/toggle"
import { useTheme } from "next-themes"
import { Sun, Moon, Trash2 } from "lucide-react"
import { useState, useEffect } from "react"

export default function SettingsPage() {
  const { theme, setTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-2xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Settings</h1>
          <p className="text-muted-foreground">Manage your preferences and account settings</p>
        </div>

        {/* Theme Settings */}
        <Card className="p-6">
          <h2 className="text-lg font-semibold mb-4">Appearance</h2>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <label className="text-sm font-medium">Theme</label>
              {mounted && (
                <div className="flex gap-2">
                  <Toggle pressed={theme === "light"} onPressedChange={() => setTheme("light")} className="gap-2">
                    <Sun className="w-4 h-4" />
                    Light
                  </Toggle>
                  <Toggle pressed={theme === "dark"} onPressedChange={() => setTheme("dark")} className="gap-2">
                    <Moon className="w-4 h-4" />
                    Dark
                  </Toggle>
                </div>
              )}
            </div>
          </div>
        </Card>

        {/* Data Settings */}
        <Card className="p-6 border-destructive/20">
          <h2 className="text-lg font-semibold mb-4">Data & Privacy</h2>
          <div className="space-y-4">
            <p className="text-sm text-muted-foreground">
              Clear all uploaded datasets and analysis history from your account.
            </p>
            <Button variant="destructive" className="gap-2">
              <Trash2 className="w-4 h-4" />
              Clear All Data
            </Button>
          </div>
        </Card>

        {/* API Settings */}
        <Card className="p-6">
          <h2 className="text-lg font-semibold mb-4">API Configuration</h2>
          <div className="space-y-4">
            <div>
              <label className="text-sm font-medium block mb-2">Backend URL</label>
              <input
                type="text"
                placeholder="https://api.example.com"
                className="w-full px-3 py-2 border border-input rounded-md bg-background text-foreground"
              />
            </div>
            <div>
              <label className="text-sm font-medium block mb-2">API Key (Optional)</label>
              <input
                type="password"
                placeholder="Enter your API key"
                className="w-full px-3 py-2 border border-input rounded-md bg-background text-foreground"
              />
            </div>
            <Button>Save Configuration</Button>
          </div>
        </Card>
      </div>
    </div>
  )
}
