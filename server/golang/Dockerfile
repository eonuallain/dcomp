# see https://github.com/chemidy/smallest-secured-golang-docker-image

FROM golang:1.14-alpine3.11

# Install git + SSL ca certificates.
# Git is required for fetching the dependencies.
# Ca-certificates is required to call HTTPS endpoints.
RUN apk update && apk add --no-cache git ca-certificates tzdata bash && update-ca-certificates

# Create appuser
ENV USER=appuser
ENV UID=10001

# See https://stackoverflow.com/a/55757473/12429735
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
WORKDIR .

COPY docker-entry.sh /go/bin/docker-entry.sh
COPY server-main.go .

# Fetch dependencies.
RUN go get -d -v

# Build the binary
RUN go build -o /go/bin/dcomp-server .
#RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm go build \
#      -ldflags='-w -s -extldflags "-static"' -a \
#      -o /go/bin/dcomp-server .

# Use an unprivileged user.
USER appuser:appuser

# Run the hello binary.
ENTRYPOINT ["/go/bin/docker-entry.sh"]
