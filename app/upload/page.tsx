"use client"

import type React from "react"

import { useState, useRef } from "react"
import { Upload, AlertCircle, CheckCircle } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { useEDA } from "@/lib/context"
import { useRouter } from "next/navigation"

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string[]>([])
  const [localError, setLocalError] = useState<string>("")
  const [loading, setLoading] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const { uploadDataset } = useEDA()
  const router = useRouter()

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0]
    if (selectedFile) {
      validateAndLoadFile(selectedFile)
    }
  }

  const validateAndLoadFile = (selectedFile: File) => {
    setLocalError("")

    // Validate file type
    if (!selectedFile.name.endsWith(".csv")) {
      setLocalError("Please upload a CSV file")
      return
    }

    // Validate file size (max 50MB)
    if (selectedFile.size > 50 * 1024 * 1024) {
      setLocalError("File size must be less than 50MB")
      return
    }

    // Validate file is not empty
    if (selectedFile.size === 0) {
      setLocalError("File is empty")
      return
    }

    setFile(selectedFile)

    // Parse preview
    const reader = new FileReader()
    reader.onload = (e) => {
      const text = e.target?.result as string
      const lines = text.split("\n")
      setPreview(lines.slice(0, 6))
    }
    reader.readAsText(selectedFile)
  }

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    const droppedFile = e.dataTransfer.files[0]
    if (droppedFile) {
      validateAndLoadFile(droppedFile)
    }
  }

  const handleAnalyze = async () => {
    if (!file) return

    setLoading(true)
    try {
      await uploadDataset(file)
      // Redirect to profiling page
      setTimeout(() => {
        router.push("/profiling")
      }, 1000)
    } catch (error) {
      setLocalError("Failed to upload dataset. Please try again.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-2xl mx-auto space-y-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Upload Dataset</h1>
          <p className="text-muted-foreground">Upload your CSV file to begin exploratory data analysis</p>
        </div>

        {/* Upload Zone */}
        <Card
          className="border-2 border-dashed cursor-pointer transition-colors hover:border-primary/50"
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          onClick={() => fileInputRef.current?.click()}
        >
          <div className="p-12 text-center">
            <Upload className="w-12 h-12 mx-auto mb-4 text-muted-foreground" />
            <h3 className="font-semibold text-lg mb-1">Drag and drop your CSV</h3>
            <p className="text-muted-foreground mb-4">or click to browse</p>
            <p className="text-sm text-muted-foreground">Maximum file size: 50MB</p>
          </div>
          <input ref={fileInputRef} type="file" accept=".csv" onChange={handleFileChange} className="hidden" />
        </Card>

        {/* Error State */}
        {localError && (
          <Alert variant="destructive">
            <AlertCircle className="w-4 h-4" />
            <AlertDescription>{localError}</AlertDescription>
          </Alert>
        )}

        {/* File Info */}
        {file && (
          <div className="space-y-4">
            <div className="flex items-center gap-3 p-4 rounded-lg bg-muted">
              <CheckCircle className="w-5 h-5 text-green-600" />
              <div>
                <p className="font-semibold">{file.name}</p>
                <p className="text-sm text-muted-foreground">{(file.size / 1024).toFixed(2)} KB</p>
              </div>
            </div>

            {/* Preview Table */}
            {preview.length > 0 && (
              <Card className="p-4">
                <h3 className="font-semibold mb-3">Preview (first 5 rows)</h3>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <tbody>
                      {preview.slice(0, 6).map((row, idx) => (
                        <tr key={idx} className={idx === 0 ? "font-semibold border-b" : ""}>
                          {row.split(",").map((cell, cellIdx) => (
                            <td key={cellIdx} className="p-2 border-r last:border-r-0">
                              {cell.substring(0, 20)}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </Card>
            )}

            <Button onClick={handleAnalyze} size="lg" className="w-full" disabled={loading}>
              {loading ? "Analyzing..." : "Upload and Analyze"}
            </Button>
          </div>
        )}
      </div>
    </div>
  )
}
