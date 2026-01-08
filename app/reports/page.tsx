"use client"

import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { FileJson, FileText, Download } from "lucide-react"

const reports = [
  {
    title: "Full EDA Report",
    description: "Complete profiling and analysis summary",
    icon: FileText,
    format: "PDF",
    action: () => {
      console.log("Downloading Full EDA Report as PDF")
    },
  },
  {
    title: "Data Profile",
    description: "Detailed column-level statistics",
    icon: FileJson,
    format: "JSON",
    action: () => {
      console.log("Downloading Data Profile as JSON")
    },
  },
  {
    title: "Risk Assessment",
    description: "Data quality and risk evaluation",
    icon: FileText,
    format: "PDF",
    action: () => {
      console.log("Downloading Risk Assessment as PDF")
    },
  },
  {
    title: "Cleaning Script",
    description: "Python script for data cleaning",
    icon: FileText,
    format: "PY",
    action: () => {
      console.log("Downloading Cleaning Script as PY")
    },
  },
]

export default function ReportsPage() {
  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Reports & Export</h1>
          <p className="text-muted-foreground">Download comprehensive analysis reports and scripts</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {reports.map((report) => {
            const Icon = report.icon
            return (
              <Card key={report.title} className="p-6 flex flex-col">
                <div className="flex items-start gap-4 mb-6 flex-1">
                  <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                    <Icon className="w-6 h-6 text-primary" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-lg">{report.title}</h3>
                    <p className="text-sm text-muted-foreground">{report.description}</p>
                  </div>
                </div>
                <Button className="gap-2 w-full" onClick={report.action}>
                  <Download className="w-4 h-4" />
                  Download {report.format}
                </Button>
              </Card>
            )
          })}
        </div>
      </div>
    </div>
  )
}
