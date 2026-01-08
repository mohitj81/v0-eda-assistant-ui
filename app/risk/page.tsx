"use client"

import { useEffect } from "react"
import { Card } from "@/components/ui/card"
import { useEDA } from "@/lib/context"
import { RiskMeter, IssueAlert, PageSkeleton } from "@/components/custom"

export default function RiskPage() {
  const { currentDataset, riskAssessment, loading, fetchRiskAssessment } = useEDA()

  useEffect(() => {
    if (currentDataset?.id && !riskAssessment) {
      fetchRiskAssessment(currentDataset.id)
    }
  }, [currentDataset, riskAssessment, fetchRiskAssessment])

  if (loading) {
    return (
      <div className="min-h-screen bg-background p-6 md:p-12">
        <div className="max-w-4xl mx-auto">
          <PageSkeleton />
        </div>
      </div>
    )
  }

  const risk = riskAssessment || {
    score: "Medium",
    numeric_score: 53,
    critical_issues: [
      "High missing values in Age column (1.2%) - may affect numerical models",
      "Inconsistent data format in Salary column - contains mixed formats",
    ],
    warnings: ["15 duplicate rows detected - review before analysis"],
  }

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Data Quality Risk Assessment</h1>
          <p className="text-muted-foreground">Identify potential data quality issues and their impact</p>
        </div>

        {/* Risk Score */}
        <Card className="p-8">
          <RiskMeter score={risk.score} percentage={Math.round(risk.numeric_score)} />
        </Card>

        {/* Critical Issues */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold">Critical Issues</h2>
          {risk.critical_issues.map((issue, idx) => (
            <IssueAlert key={idx} level="critical" description={issue} />
          ))}
        </div>

        {/* Warnings */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold">Warnings</h2>
          {risk.warnings.map((warning, idx) => (
            <IssueAlert key={idx} level="warning" description={warning} />
          ))}
        </div>

        {/* Recommendations */}
        <Card className="p-6 bg-primary/5 border-primary/20">
          <h2 className="text-lg font-bold mb-4">Recommended Actions</h2>
          <ul className="space-y-2 text-sm">
            <li className="flex gap-2">
              <span className="text-primary font-bold">1.</span>
              <span>Fill missing values in Age using median imputation</span>
            </li>
            <li className="flex gap-2">
              <span className="text-primary font-bold">2.</span>
              <span>Standardize Salary format to consistent decimal places</span>
            </li>
            <li className="flex gap-2">
              <span className="text-primary font-bold">3.</span>
              <span>Remove duplicate rows before analysis</span>
            </li>
          </ul>
        </Card>
      </div>
    </div>
  )
}
