"use client"

import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

interface RiskMeterProps {
  score: "Low" | "Medium" | "High"
  percentage: number
  className?: string
}

export function RiskMeter({ score, percentage, className }: RiskMeterProps) {
  const getRiskColor = (riskScore: string) => {
    switch (riskScore) {
      case "Low":
        return "bg-green-600"
      case "Medium":
        return "bg-yellow-600"
      case "High":
        return "bg-destructive"
      default:
        return "bg-muted"
    }
  }

  const getBadgeColor = (riskScore: string) => {
    switch (riskScore) {
      case "Low":
        return "bg-green-600 text-white"
      case "Medium":
        return "bg-yellow-600 text-white"
      case "High":
        return "bg-destructive text-white"
      default:
        return ""
    }
  }

  return (
    <div className={cn("space-y-3", className)}>
      <div className="flex items-center justify-between">
        <h3 className="font-semibold">Risk Score</h3>
        <Badge className={getBadgeColor(score)}>{score}</Badge>
      </div>

      <div className="space-y-2">
        <div className="flex justify-between text-sm">
          <span className="text-muted-foreground">Risk Level</span>
          <span className="font-medium">{percentage}%</span>
        </div>

        <div className="w-full bg-muted rounded-full h-3 overflow-hidden">
          <div
            className={cn("h-full transition-all duration-300", getRiskColor(score))}
            style={{ width: `${percentage}%` }}
          />
        </div>
      </div>

      {/* Risk Level Labels */}
      <div className="flex justify-between text-xs text-muted-foreground pt-2">
        <span>Low (0%)</span>
        <span>Medium (50%)</span>
        <span>High (100%)</span>
      </div>
    </div>
  )
}
