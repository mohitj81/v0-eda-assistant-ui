"use client"

import type React from "react"

import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { cn } from "@/lib/utils"

interface Column {
  key: string
  label: string
  render?: (value: any) => React.ReactNode
  className?: string
}

interface DataTableProps {
  columns: Column[]
  data: Record<string, any>[]
  className?: string
  highlightKey?: string
}

export function DataTable({ columns, data, className, highlightKey }: DataTableProps) {
  return (
    <div className={cn("rounded-lg border overflow-hidden", className)}>
      <Table>
        <TableHeader className="bg-muted">
          <TableRow>
            {columns.map((col) => (
              <TableHead key={col.key} className={col.className}>
                {col.label}
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((row, rowIdx) => (
            <TableRow
              key={rowIdx}
              className={cn(
                "hover:bg-muted/50 transition-colors",
                highlightKey && row[highlightKey] ? "bg-destructive/5" : "",
              )}
            >
              {columns.map((col) => (
                <TableCell key={`${rowIdx}-${col.key}`} className={col.className}>
                  {col.render ? col.render(row[col.key]) : row[col.key]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
