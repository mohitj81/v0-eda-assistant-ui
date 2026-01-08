"use client"

import Link from "next/link"
import { ArrowRight, Upload, BarChart3, AlertTriangle, Zap, Download } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"

const features = [
  {
    icon: BarChart3,
    title: "Data Profiling",
    description: "Comprehensive analysis of your dataset structure, data types, and distributions",
  },
  {
    icon: AlertTriangle,
    title: "Risk Assessment",
    description: "Identify data quality issues and potential downstream impacts",
  },
  {
    icon: Zap,
    title: "AI Insights",
    description: "Get intelligent explanations and recommendations for data cleaning",
  },
  {
    icon: Download,
    title: "Script Generation",
    description: "Auto-generate Python scripts to clean and prepare your data",
  },
]

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <section className="px-6 py-20 md:px-12 md:py-28 max-w-6xl mx-auto">
        <div className="text-center space-y-6">
          <div className="inline-block px-4 py-2 rounded-full bg-primary/10 border border-primary/20">
            <p className="text-sm text-primary font-medium">Automated Data Analysis</p>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-balance">
            Exploratory Data Analysis,{" "}
            <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">Simplified</span>
          </h1>

          <p className="text-lg text-muted-foreground max-w-2xl mx-auto text-balance">
            Upload your CSV, discover insights, assess data quality, and get Python scripts to clean your data—all in
            one platform.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
            <Link href="/upload">
              <Button size="lg" className="gap-2">
                <Upload className="w-5 h-5" />
                Upload Dataset
              </Button>
            </Link>
            <Button size="lg" variant="outline">
              View Documentation <ArrowRight className="w-4 h-4" />
            </Button>
          </div>
        </div>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-20">
          {features.map((feature) => {
            const Icon = feature.icon
            return (
              <Card key={feature.title} className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                    <Icon className="w-6 h-6 text-primary" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
                    <p className="text-muted-foreground">{feature.description}</p>
                  </div>
                </div>
              </Card>
            )
          })}
        </div>
      </section>
    </div>
  )
}
