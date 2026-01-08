"use client"

import { useEffect } from "react"
import { Card } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import { useEDA } from "@/lib/context"
import { MetricCard, PageSkeleton } from "@/components/custom"

export default function ProfilingPage() {
  const { currentDataset, profiling, loading, fetchProfilingResults } = useEDA()

  useEffect(() => {
    if (currentDataset?.id && !profiling) {
      fetchProfilingResults(currentDataset.id)
    }
  }, [currentDataset, profiling, fetchProfilingResults])

  if (loading) {
    return (
      <div className="min-h-screen bg-background p-6 md:p-12">
        <div className="max-w-6xl mx-auto">
          <PageSkeleton />
        </div>
      </div>
    )
  }

  const mockData = profiling || {
    summary: {
      rows: 1000,
      columns: 12,
      missing_percentage: 8.2,
      duplicate_rows: 15,
    },
    columns: [
      { name: "Age", dtype: "int", missing: 12, unique: 42, examples: "25, 30, 45" },
      { name: "Salary", dtype: "float", missing: 5, unique: 987, examples: "50000.00, 65000.00" },
      { name: "Department", dtype: "string", missing: 0, unique: 8, examples: "Sales, IT, HR" },
      { name: "Hire_Date", dtype: "date", missing: 3, unique: 456, examples: "2020-01-15, 2019-05-20" },
    ],
  }

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-6xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Data Profiling Summary</h1>
          <p className="text-muted-foreground">Detailed analysis of your dataset structure and quality</p>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <MetricCard label="Total Rows" value={mockData.summary.rows.toLocaleString()} />
          <MetricCard label="Total Columns" value={mockData.summary.columns} />
          <MetricCard label="Missing Values" value={`${mockData.summary.missing_percentage}%`} />
          <MetricCard label="Duplicate Rows" value={mockData.summary.duplicate_rows} />
        </div>

        {/* Detailed Analysis */}
        <Tabs defaultValue="summary" className="space-y-4">
          <TabsList>
            <TabsTrigger value="summary">Summary</TabsTrigger>
            <TabsTrigger value="missing">Missing Values</TabsTrigger>
            <TabsTrigger value="duplicates">Duplicates</TabsTrigger>
            <TabsTrigger value="types">Data Types</TabsTrigger>
          </TabsList>

          <TabsContent value="summary">
            <Card className="overflow-hidden">
              <table className="w-full text-sm">
                <thead className="border-b bg-muted">
                  <tr>
                    <th className="px-6 py-3 text-left font-semibold">Column Name</th>
                    <th className="px-6 py-3 text-left font-semibold">Data Type</th>
                    <th className="px-6 py-3 text-left font-semibold">Missing</th>
                    <th className="px-6 py-3 text-left font-semibold">Unique</th>
                    <th className="px-6 py-3 text-left font-semibold">Examples</th>
                  </tr>
                </thead>
                <tbody>
                  {mockData.columns.map((col) => (
                    <tr key={col.name} className="border-b hover:bg-muted/50">
                      <td className="px-6 py-3 font-medium">{col.name}</td>
                      <td className="px-6 py-3">
                        <Badge variant="outline">{col.dtype}</Badge>
                      </td>
                      <td className="px-6 py-3">
                        {col.missing > 0 && <span className="text-destructive font-medium">{col.missing}</span>}
                        {col.missing === 0 && <span className="text-green-600">0</span>}
                      </td>
                      <td className="px-6 py-3">{col.unique}</td>
                      <td className="px-6 py-3 text-muted-foreground">{col.examples}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </Card>
          </TabsContent>

          <TabsContent value="missing">
            <Card className="p-6">
              <p className="text-muted-foreground">Missing value analysis and patterns</p>
            </Card>
          </TabsContent>

          <TabsContent value="duplicates">
            <Card className="p-6">
              <p className="text-muted-foreground">Duplicate record detection and analysis</p>
            </Card>
          </TabsContent>

          <TabsContent value="types">
            <Card className="p-6">
              <p className="text-muted-foreground">Data type distribution and inconsistencies</p>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}
