"use client"

import { Alert, AlertDescription } from "@/components/ui/alert"
import { AlertTriangle, AlertCircle, CheckCircle2 } from "lucide-react"
import { cn } from "@/lib/utils"

type IssueLevel = "critical" | "warning" | "info" | "success"

interface IssueAlertProps {
  level: IssueLevel
  title?: string
  description: string
  className?: string
}

export function IssueAlert({ level, title, description, className }: IssueAlertProps) {
  const configs = {
    critical: {
      icon: AlertTriangle,
      className: "border-destructive/50 bg-destructive/10",
      titleClassName: "text-destructive font-semibold",
      descriptionClassName: "text-destructive/90",
    },
    warning: {
      icon: AlertCircle,
      className: "border-yellow-600/50 bg-yellow-600/10",
      titleClassName: "text-yellow-700 font-semibold",
      descriptionClassName: "text-yellow-700/90",
    },
    info: {
      icon: AlertCircle,
      className: "border-blue-600/50 bg-blue-600/10",
      titleClassName: "text-blue-700 font-semibold",
      descriptionClassName: "text-blue-700/90",
    },
    success: {
      icon: CheckCircle2,
      className: "border-green-600/50 bg-green-600/10",
      titleClassName: "text-green-700 font-semibold",
      descriptionClassName: "text-green-700/90",
    },
  }

  const config = configs[level]
  const Icon = config.icon

  return (
    <Alert className={cn(config.className, className)}>
      <Icon className={cn("w-4 h-4", config.titleClassName)} />
      <AlertDescription className="ml-3">
        {title && <div className={config.titleClassName}>{title}</div>}
        <div className={config.descriptionClassName}>{description}</div>
      </AlertDescription>
    </Alert>
  )
}
