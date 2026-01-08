"use client"

import { Card } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import type { ReactNode } from "react"
import { cn } from "@/lib/utils"

interface MetricCardProps {
  label: string
  value: string | number
  icon?: ReactNode
  trend?: {
    value: number
    isPositive: boolean
  }
  className?: string
}

export function MetricCard({ label, value, icon, trend, className }: MetricCardProps) {
  return (
    <Card className={cn("p-4", className)}>
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1">
          <p className="text-sm text-muted-foreground mb-1">{label}</p>
          <div className="flex items-baseline gap-2">
            <p className="text-2xl font-bold">{value}</p>
            {trend && (
              <Badge variant="outline" className={trend.isPositive ? "bg-green-600/10" : "bg-destructive/10"}>
                {trend.isPositive ? "+" : "-"}
                {trend.value}%
              </Badge>
            )}
          </div>
        </div>
        {icon && <div className="w-10 h-10 text-muted-foreground">{icon}</div>}
      </div>
    </Card>
  )
}
