# Data-in-QR: Printable QR Labels That Carry Their Own Data

<img width="265" height="498" alt="reader" src="https://github.com/user-attachments/assets/bb605a86-29df-42bb-a6dc-3b35544885cd" />



**Printable QR labels that carry their own
data.** Scan a label to view and copy its contents in a
browser---without maintaining a backend database or relying on a
dedicated app.

## Try it now
Make a small csv file containing a column named id 

```
id,make,model,link,notes
101,Acme,Widget X-1,https://example.com/item/101,Tool bench unit
102,Logi,MX Master 3S,https://example.com/item/102,Desk setup
103,Bosch,Laser Measure,https://example.com/item/103,Field toolkit
```
Drop it onto our demo page

[https://tooltechgeek.github.io/nodb_table/csv_to_qr_generator.html]

Click 'Generate QR code'

Scan the generated QR codes



## How It Works: Serverless Data Transport via URL Hash

This project implements a lightweight, database-free architecture for conveying and extracting structured data straight from a QR code. By leveraging standard client-side web technologies and the URL fragment identifier, the system operates entirely without backend infrastructure, server databases, or companion apps.

### Core Mechanics

1. **Encoded URL Structure**: The QR code encodes a static web page URL paired with a URL hash fragment (e.g., `[http://www.example.org/foo.html#bar](http://www.example.org/foo.html#bar)`).


2. **Static Hosting**: The base URL points to a lightweight, standalone HTML/JS reader hosted statically (such as on GitHub Pages). Because hash fragments are processed exclusively on the client side, the payload is never transmitted to a server.


3. **Client-Side Extraction**: When a user scans the QR code, their mobile browser loads the static reader script, which instantly parses the data payload contained within the URL hash (`#bar`).


4. **Interactive Presentation**: The client-side script decodes the fragment and renders a clean, mobile-friendly interface equipped with one-tap **Copy** buttons for individual fields as well as a **Copy All** action.

5. **Open source QR code generator included**: We also include an auxiliar HTML/JS based generator. Drag and drop a csv file and instantly get printable labels formatted for standard adhesive label templates. 


## Why use this instead of a database-backed QR system?

-   **No backend database required:** The record travels inside the QR
    code instead of being fetched from a server-side record store.
-   **No app to install:** Ready to use from any mobile phone/tablet. 
-   **Use generic software to generate labels:** Use a spreadsheet or text editor to prepare the data
    and a browser to generate them.
-   **Portable records:** Anyone who can access the reader can view and
    copy the embedded data without needing an account in a dedicated
    application.
-   **Useful for stable information:** The printed label can continue to
    carry its record without depending on a hosted database remaining
    available.
-   **Multiple fields per code:** Store a small structured record rather
    than only a single identifier or URL.

QR codes can also store data directly, and not every conventional QR
solution requires a database. This project's particular combination is
CSV-based generation, printable labels, an embedded structured record,
and a reusable browser-based reader.

## Limitations and design considerations

-   **The data is static.** If a record changes, you will normally need
    to generate and print a replacement QR code.
-   **QR codes have limited capacity.** Larger records create denser
    codes that may be harder to scan, particularly on small labels.
-   **There is no built-in global search.** Scanning a label displays
    the record in that code; it does not automatically search across all
    generated records.
-   **The payload is not confidential.** Base64URL is an encoding
    format, not encryption. Anyone who obtains the QR code may be able
    to decode its contents. Do not embed passwords, secrets, or
    sensitive information.
-   **Offline use depends on reader availability.** A hosted reader must
    be loaded from its URL. To scan without internet access, the reader
    page and required files must be cached or already be available locally in a
    suitable setup.
-   **No synchronization is provided.** The system does not
    automatically synchronize changes between a CSV file, printed
    labels, or other applications.

For these reasons, the project is most appropriate for small, relatively
stable, non-sensitive records---not live inventory counts, access
control, or workflows that require audit trails and centralized updates.

## Project files

| File | Purpose |
| :--- | :--- |
| `csv_to_qr_generator.html` | Generator interface for importing CSV data, previewing QR codes, and creating label output. |
| `index.html` | Reader page that decodes the embedded payload and displays the record. |
| `qrcode.js` | JavaScript library used to render QR codes locally in the browser (see reference below). |
| `pdf-lib.js` | JavaScript library used to create PDF label sheets in the browser (see reference below). |

The JavaScript libraries need to be available in the locations expected
by the HTML files.

## External JavaScript libraries

This project uses the following open-source client-side libraries:

-   [qrcodejs](https://github.com/davidshimjs/qrcodejs) --- QR code
    generation in the browser.
-   [pdf-lib](https://github.com/hopding/pdf-lib) --- Creation and
    modification of PDF documents in JavaScript.

## Contributing

Suggestions and contributions are welcome. Helpful areas include:

-   Additional printable label templates.
-   Example CSV files for different use cases.
-   Improvements to the reader interface and documentation.
-   Testing with different browsers, phones, and printers.
-   Ideas that make the tool easier to use.

Please check the repository's issue tracker, if enabled, before opening
a new issue so that related suggestions can be discussed together.

## License

See the repository's license file for the terms under which this project
may be used, modified, and distributed.

## Disclaimer

Avery is a trademark of Avery Products Corporation. This software is not
affiliated with, sponsored by, or endorsed by Avery Products
Corporation.
