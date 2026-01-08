// Types for the EDA Assistant application

export interface Dataset {
  id: string
  filename: string
  size: number
  uploadedAt: Date
  rows: number
  columns: number
}

export interface ColumnAnalysis {
  name: string
  dtype: string
  missing_count: number
  missing_percentage: number
  unique_count: number
  unique_percentage: number
  mean?: number
  median?: number
  std?: number
  min?: number
  max?: number
}

export interface ProfilingResult {
  session_id: string
  rows: number
  columns: number
  duplicates: number
  duplicate_percentage: number
  memory_usage_mb: number
  columns_analysis: ColumnAnalysis[]
  generated_at: string
}

export interface RiskIssue {
  severity: "critical" | "warning" | "info"
  type: string
  column?: string
  message: string
}

export interface RiskAssessment {
  session_id: string
  risk_score: number
  risk_level: "Low" | "Medium" | "High"
  components: {
    missing_value_rate: number
    duplicate_rate: number
    datatype_issue_score: number
  }
  issues: RiskIssue[]
  generated_at: string
}

export interface ComparisonMetrics {
  rows: number
  columns: number
  missing_values: number
  missing_percentage: number
  duplicates: number
  duplicate_percentage: number
  memory_mb: number
}

export interface Comparison {
  session_id: string
  before: ComparisonMetrics
  after: ComparisonMetrics
  improvements: {
    rows_removed: number
    missing_values_fixed: number
    duplicates_removed: number
  }
  generated_at: string
}

export interface CleaningScript {
  code: string
  language: "python"
  format: "pandas"
}

export interface EDAState {
  currentDataset: Dataset | null
  profiling: ProfilingResult | null
  riskAssessment: RiskAssessment | null
  cleaningScript: CleaningScript | null
  explanation: string | null
  comparison: Comparison | null
  loading: boolean
  error: string | null
}
