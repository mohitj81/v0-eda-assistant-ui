"use client"

import { useEffect } from "react"
import { useEDA } from "@/lib/context"
import { CodeBlock, PageSkeleton, IssueAlert } from "@/components/custom"

const defaultScript = `import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("input.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values in Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Standardize Salary format
df['Salary'] = df['Salary'].astype(float).round(2)

# Validate data types
df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])

# Save cleaned dataset
df.to_csv("cleaned_output.csv", index=False)

print("Data cleaning complete!")
print(f"Cleaned rows: {len(df)}")
print(f"Cleaned columns: {len(df.columns)}")`

export default function ScriptPage() {
  const { currentDataset, cleaningScript, loading, fetchCleaningScript } = useEDA()

  useEffect(() => {
    if (currentDataset?.id && !cleaningScript) {
      fetchCleaningScript(currentDataset.id)
    }
  }, [currentDataset, cleaningScript, fetchCleaningScript])

  if (loading) {
    return (
      <div className="min-h-screen bg-background p-6 md:p-12">
        <div className="max-w-4xl mx-auto">
          <PageSkeleton />
        </div>
      </div>
    )
  }

  const script = cleaningScript?.code || defaultScript

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Python Cleaning Script</h1>
          <p className="text-muted-foreground">Auto-generated script to replicate cleaning steps</p>
        </div>

        <CodeBlock code={script} language="python" filename="clean_data.py" />

        <IssueAlert
          level="warning"
          title="Execution Required"
          description="This script must be executed in your local Python environment. Ensure pandas and numpy are installed."
        />
      </div>
    </div>
  )
}
