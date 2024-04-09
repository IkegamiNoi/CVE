import scrapy

# nvdからの取得はsettings.pyで「ROBOTSTXT_OBEY = False」にしておく
class NvdCvssSpider(scrapy.Spider):
    name = "nvd_cvss"
    allowed_domains = ["nvd.nist.gov/vuln/detail/CVE-2023-20269"]
    start_urls = ["https://nvd.nist.gov/vuln/detail/CVE-2023-20269"]

    def parse(self, response):
        cvss = response.xpath("//span[@class='tooltipCvss3NistMetrics']/text()")
        yield{
            'cvss':cvss
        }
        print(cvss)
