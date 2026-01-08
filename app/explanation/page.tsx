"use client"

import { useEffect, useState } from "react"
import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { RotateCw } from "lucide-react"
import { useEDA } from "@/lib/context"
import { PageSkeleton } from "@/components/custom"

export default function ExplanationPage() {
  const { currentDataset, explanation, loading, fetchExplanation } = useEDA()
  const [regenerating, setRegenerating] = useState(false)

  useEffect(() => {
    if (currentDataset?.id && !explanation) {
      fetchExplanation(currentDataset.id)
    }
  }, [currentDataset, explanation, fetchExplanation])

  const handleRegenerate = async () => {
    if (!currentDataset?.id) return
    setRegenerating(true)
    try {
      await fetchExplanation(currentDataset.id)
    } finally {
      setRegenerating(false)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-background p-6 md:p-12">
        <div className="max-w-4xl mx-auto">
          <PageSkeleton />
        </div>
      </div>
    )
  }

  const defaultExplanation =
    explanation ||
    `Your dataset contains 1,000 rows across 12 columns with an overall data quality score of 53% (Medium risk). The main issues identified are missing values in the Age column (1.2%) and inconsistent formatting in the Salary column. There are also 15 duplicate rows that should be removed before analysis.`

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold mb-2">AI Insights</h1>
            <p className="text-muted-foreground">Intelligent analysis and recommendations</p>
          </div>
          <Button
            variant="outline"
            size="sm"
            className="gap-2 bg-transparent"
            onClick={handleRegenerate}
            disabled={regenerating}
          >
            <RotateCw className={`w-4 h-4 ${regenerating ? "animate-spin" : ""}`} />
            {regenerating ? "Regenerating..." : "Regenerate"}
          </Button>
        </div>

        {/* Main Explanation */}
        <Card className="p-6 space-y-6">
          <div>
            <h2 className="text-lg font-bold mb-3">Data Quality Overview</h2>
            <div className="prose prose-invert max-w-none text-foreground">
              <p className="text-muted-foreground leading-relaxed">{defaultExplanation}</p>
            </div>
          </div>

          <div className="border-t pt-6">
            <h2 className="text-lg font-bold mb-3">Issues Found</h2>
            <ul className="space-y-2 text-muted-foreground">
              <li className="flex gap-3">
                <span className="text-destructive font-bold">•</span>
                <span>
                  <strong>Missing Values:</strong> Age column has 12 missing values (1.2%)
                </span>
              </li>
              <li className="flex gap-3">
                <span className="text-destructive font-bold">•</span>
                <span>
                  <strong>Format Inconsistency:</strong> Salary column contains mixed decimal formats
                </span>
              </li>
              <li className="flex gap-3">
                <span className="text-yellow-600 font-bold">•</span>
                <span>
                  <strong>Duplicates:</strong> 15 duplicate rows detected across dataset
                </span>
              </li>
            </ul>
          </div>

          <div className="border-t pt-6">
            <h2 className="text-lg font-bold mb-3">Impact & Recommendations</h2>
            <div className="space-y-4 text-muted-foreground">
              <p>These data quality issues could impact downstream machine learning models and analysis:</p>
              <ul className="space-y-2 list-disc list-inside">
                <li>Missing values may bias statistical calculations</li>
                <li>Inconsistent formats could cause type conversion errors</li>
                <li>Duplicates may introduce bias and skew model training</li>
              </ul>
            </div>
          </div>

          <div className="border-t pt-6 bg-primary/5 -mx-6 -mb-6 px-6 py-6 rounded-b-lg">
            <h2 className="text-lg font-bold mb-3">Recommended Actions</h2>
            <ol className="space-y-2 text-muted-foreground list-decimal list-inside">
              <li>Fill missing Age values using median imputation</li>
              <li>Standardize Salary to 2 decimal places</li>
              <li>Remove the 15 identified duplicate rows</li>
              <li>Validate data types across all columns</li>
            </ol>
          </div>
        </Card>
      </div>
    </div>
  )
}
