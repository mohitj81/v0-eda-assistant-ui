"use client"

import { Card } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function ComparisonPage() {
  const comparisonData = [
    {
      metric: "Missing Values",
      before: "8.2%",
      after: "2.1%",
      improvement: "-6.1%",
      improvementClass: "bg-green-600/10",
    },
    {
      metric: "Duplicate Rows",
      before: "15 (1.5%)",
      after: "0 (0%)",
      improvement: "-15 rows",
      improvementClass: "bg-green-600/10",
    },
    {
      metric: "Type Inconsistencies",
      before: "3",
      after: "0",
      improvement: "-3",
      improvementClass: "bg-green-600/10",
    },
    {
      metric: "Data Quality Score",
      before: "53%",
      after: "87%",
      improvement: "+34%",
      improvementClass: "bg-green-600/10",
    },
  ]

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-6xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Before & After Comparison</h1>
          <p className="text-muted-foreground">Visualize the improvements from data cleaning</p>
        </div>

        {/* Comparison Table */}
        <Card className="overflow-hidden">
          <table className="w-full text-sm">
            <thead className="border-b bg-muted">
              <tr>
                <th className="px-6 py-3 text-left font-semibold">Metric</th>
                <th className="px-6 py-3 text-left font-semibold">Before</th>
                <th className="px-6 py-3 text-left font-semibold">After</th>
                <th className="px-6 py-3 text-left font-semibold">Improvement</th>
              </tr>
            </thead>
            <tbody>
              {comparisonData.map((row) => (
                <tr key={row.metric} className="border-b hover:bg-muted/50">
                  <td className="px-6 py-3 font-medium">{row.metric}</td>
                  <td className="px-6 py-3">{row.before}</td>
                  <td className="px-6 py-3 text-green-600">{row.after}</td>
                  <td className="px-6 py-3">
                    <Badge variant="outline" className={row.improvementClass}>
                      {row.improvement}
                    </Badge>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        {/* Summary */}
        <Card className="p-6 bg-green-600/5 border-green-600/20">
          <h2 className="text-lg font-bold mb-2 text-green-600">Cleaning Summary</h2>
          <p className="text-muted-foreground">
            Data cleaning successfully improved quality from 53% to 87%. All identified issues have been resolved,
            preparing your dataset for analysis and machine learning applications.
          </p>
        </Card>
      </div>
    </div>
  )
}
