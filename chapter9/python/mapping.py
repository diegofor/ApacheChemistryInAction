# From Alfresco to OpenCMIS InMemory
mapping = {'D:cmisbook:image':
                 {
                     'targetType': 'cmisbook:image',
                     'properties': {'cmisbook:gpsLatitude': 'cmisbook:gpsLatitude',
                                    'cmisbook:subjectDistance': 'cmisbook:subjectDistance',
                                    'cmisbook:brightnessValue': 'cmisbook:brightnessValue',
                                    'cmisbook:exposureProgram': 'cmisbook:exposureProgram',
                                    'cmisbook:imageDescription': 'cmisbook:imageDescription',
                                    'cmisbook:gpsAltitudeRef': 'cmisbook:gpsAltitudeRef',
                                    'cmisbook:focalLength': 'cmisbook:focalLength',
                                    'cmisbook:createDate': 'cmisbok:createDate',
                                    'cmisbook:bitsPerSample': 'cmisbook:bitsPerSample',
                                    'cmisbook:dataPrecision': 'cmisbook:dataPrecision',
                                    'cmisbook:yCbCrPositioning': 'cmisbook:yCbCrPositioning',
                                    'cmisbook:flash': 'cmisbook:flash',
                                    'cmisbook:lightSource': 'cmisbook:lightSource',
                                    'cmisbook:tags': 'cmisbook:tags',
                                    'cmisbook:userComment': 'cmisbook:userComment',
                                    'cmisbook:exposureMode': 'cmisbook:exposureMode',
                                    'cmisbook:model': 'cmisbook:model',
                                    'cmisbook:gpsAltitude': 'cmisbook:gpsAltitude',
                                    'cmisbook:exposureTime': 'cmisbook:exposureTime',
                                    'cmisbook:rating': 'cmisbook:rating',
                                    'cmisbook:imageArtist': 'cmisbook:imageArtist',
                                    'cmisbook:ownerName': 'cmisbook:ownerName',
                                    'cmisbook:pixelXDimension': 'cmisbook:pixelXDimension',
                                    'cmisbook:shutterSpeedValue': 'cmisbook:shutterSpeedValue',
                                    'cmisbook:make': 'cmisbook:make',
                                    'cmisbook:orientation': 'cmisbook:orientation',
                                    'cmisbook:xResolution': 'cmisbook:xResolution',
                                    'cmisbook:resolutionUnit': 'cmisbook:resolutionUnit',
                                    'cmisbook:compression': 'cmisbook:compression',
                                    'cmisbook:whiteBalance': 'cmisbook:whiteBalance',
                                    'cmisbook:pixelYDimension': 'cmisbook:pixelYDimension',
                                    'cmisbook:fNumber': 'cmisbook:fNumber',
                                    'cmisbook:serialNumber': 'cmisbook:serialNumber',
                                    'cmisbook:timeZoneOffset': 'cmisbook:timeZoneOffset',
                                    'cmisbook:copyright': 'cmisbook:copyright',
                                    'cmisbook:yResolution': 'cmisbook:yResolution',
                                    'cmisbook:ratingPercent': 'cmisbook:ratingPercent',
                                    'cmisbook:exposureCompensation': 'cmisbook:exposureCompensation',
                                    'cmisbook:isoSpeed': 'cmisbook:isoSpeed',
                                    'cmisbook:dateTimeOriginal': 'cmisbook:dateTimeOriginal',
                                    'cmisbook:imageHeight': 'cmisbook:imageHeight',
                                    'cmisbook:modifyTime': 'cmisbook:modifyTime',
                                    'cmisbook:gpsLatitudeRef': 'cmisbook:latitudeRef',
                                    'cmisbook:selfTimerMode': 'cmisbook:selfTimerMode',
                                    'cmisbook:meteringMode': 'cmisbook:meteringMode',
                                    'cmisbook:apertureValue': 'cmisbook:apertureValue',
                                    'cmisbook:colorSpace': 'cmisbook:colorSpace',
                                    'cmisbook:gpsLongitudeRef': 'cmisbook:gpsLongitudeRef',
                                    'cmisbook:imageWidth': 'cmisbook:imageWidth',
                                    'cmisbook:maxApertureValue': 'cmisbook:maxApertureValue',
                                    'cmisbook:photometricInterpretation': 'cmisbook:photometricInterpretation',
                                    'cmisbook:gpsLongitude': 'cmisbook:gpsLongitude',
                                    'cmisbook:sceneCaptureType': 'cmisbook:sceneCaptureType'}
                 },
           'D:cmisbook:audio':
                 {
                    'targetType': 'cmisbook:audio',
                    'properties': {'cmisbook:album': 'cmisbook:album',
                                   'cmisbook:artist': 'cmisbook:artist',
                                   'cmisbook:artwork': 'cmisbook:artwork',
                                   'cmisbook:audioChannelType': 'cmisbook:audioChannelType',
                                   'cmisbook:audioFormat': 'cmisbook:audioFormat',
                                   'cmisbook:comment': 'cmisbook:comment',
                                   'cmisbook:composer': 'cmisbook:composer',
                                   'cmisbook:compressorVersion': 'cmisbook:compressorVersion',
                                   'cmisbook:discNo': 'cmisbook:discNo',
                                   'cmisbook:genre': 'cmisbook:genre',
                                   'cmisbook:length': 'cmisbook:length',
                                   'cmisbook:license': 'cmisbook:license',
                                   'cmisbook:noChannels': 'cmisbook:noChannels',
                                   'cmisbook:sampleRate': 'cmisbook:sampleRate',
                                   'cmisbook:sourceURL': 'cmisbook:sourceURL',
                                   'cmisbook:tags': 'cmisbook:tags',
                                   'cmisbook:title': 'cmisbook:title',
                                   'cmisbook:track': 'cmisbook:track',
                                   'cmisbook:year': 'cmisbook:year'}
                 },
           'D:cmisbook:pdf':
                 {
                     'targetType': 'cmisbook:pdf',
                     'properties': {'cmisbook:createdDate': 'cmisbook:createdDate',
                                    'cmisbook:creator': 'cmisbook:creator',
                                    'cmisbook:modifiedDate': 'cmisbook:modifiedDate',
                                    'cmisbook:noPages': 'cmisbook:noPages',
                                    'cmisbook:pdfAuthor': 'cmisbook:pdfAuthor',
                                    'cmisbook:pdfKeywords': 'cmisbook:pdfKeywords',
                                    'cmisbook:pdfTitle': 'cmisbook:pdfTitle',
                                    'cmisbook:producer': 'cmisbook:producer',
                                    'cmisbook:subject': 'cmisbook:subject',
                                    'cmisbook:trapped': 'cmisbook:trapped'}
                },
            'D:cmisbook:video':
                {
                    'targetType': 'cmisbook:video',
                    'properties': {'cmisbook:artwork': 'cmisbook:artwork',
                                   'cmisbook:audiosize': 'cmisbook:audiosize',
                                   'cmisbook:datasize': 'cmisbook:datasize',
                                   'cmisbook:hasAudio': 'cmisbook:hasAudio',
                                   'cmisbook:hasVideo': 'cmisbook:hasVideo',
                                   'cmisbook:license': 'cmisbook:license',
                                   'cmisbook:sourceURL': 'cmisbook:sourceURL',
                                   'cmisbook:tags': 'cmisbook:tags',
                                   'cmisbook:videoDuration': 'cmisbook:videoDuration',
                                   'cmisbook:videoFramerate': 'cmisbook:videoFramerate',
                                   'cmisbook:videoHeight': 'cmisbook:videoHeight',
                                   'cmisbook:videosize': 'cmisbook:videosize',
                                   'cmisbook:videoWidth': 'cmisbook:videoWidth',
                                   'cmisbook:year': 'cmisbook:year'}
                }
                
           }
