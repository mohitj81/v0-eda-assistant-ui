"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import {
  Home,
  Upload,
  BarChart3,
  AlertTriangle,
  Zap,
  GitCompare,
  Code,
  FileText,
  BookOpen,
  Settings,
  ChevronLeft,
} from "lucide-react"
import { Button } from "@/components/ui/button"

interface SidebarProps {
  open: boolean
  onOpenChange: (open: boolean) => void
}

const navItems = [
  { href: "/", label: "Home", icon: Home },
  { href: "/upload", label: "Upload Dataset", icon: Upload },
  { href: "/profiling", label: "Data Profiling", icon: BarChart3 },
  { href: "/risk", label: "Risk Assessment", icon: AlertTriangle },
  { href: "/explanation", label: "AI Insights", icon: Zap },
  { href: "/comparison", label: "Before & After", icon: GitCompare },
  { href: "/script", label: "Script Generator", icon: Code },
  { href: "/reports", label: "Reports & Export", icon: FileText },
  { href: "/documentation", label: "Documentation", icon: BookOpen },
  { href: "/settings", label: "Settings", icon: Settings },
]

export function Sidebar({ open, onOpenChange }: SidebarProps) {
  const pathname = usePathname()

  return (
    <>
      {/* Overlay for mobile */}
      {open && (
        <div
          className="fixed inset-0 z-20 md:hidden bg-background/80 backdrop-blur-sm"
          onClick={() => onOpenChange(false)}
        />
      )}

      {/* Sidebar */}
      <aside
        className={cn(
          "fixed left-0 top-0 z-30 h-screen w-64 bg-sidebar border-r border-sidebar-border flex flex-col transition-transform duration-300 md:relative md:translate-x-0",
          open ? "translate-x-0" : "-translate-x-full",
        )}
      >
        {/* Logo */}
        <div className="flex items-center justify-between h-16 px-6 border-b border-sidebar-border">
          <Link href="/" className="flex items-center gap-2 font-bold text-lg">
            <div className="w-8 h-8 bg-gradient-to-br from-primary to-accent rounded-lg flex items-center justify-center">
              <span className="text-primary-foreground text-sm font-bold">ED</span>
            </div>
            <span className="hidden sm:inline text-sidebar-foreground">EDA</span>
          </Link>
          <Button variant="ghost" size="icon" onClick={() => onOpenChange(false)} className="md:hidden">
            <ChevronLeft className="w-4 h-4" />
          </Button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 overflow-y-auto px-3 py-4 space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon
            const isActive = pathname === item.href
            return (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => {
                  // Close sidebar on mobile after navigation
                  if (window.innerWidth < 768) {
                    onOpenChange(false)
                  }
                }}
                className={cn(
                  "flex items-center gap-3 px-4 py-2 rounded-lg text-sm transition-colors",
                  isActive
                    ? "bg-sidebar-primary text-sidebar-primary-foreground"
                    : "text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
                )}
              >
                <Icon className="w-4 h-4 flex-shrink-0" />
                <span>{item.label}</span>
              </Link>
            )
          })}
        </nav>

        {/* Footer */}
        <div className="border-t border-sidebar-border p-4 space-y-2">
          <p className="text-xs text-sidebar-foreground/60">Version 1.0</p>
          <p className="text-xs text-sidebar-foreground/60">© 2026 EDA Assistant</p>
        </div>
      </aside>
    </>
  )
}
